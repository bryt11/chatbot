import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, render_template, request, redirect, url_for, session
import os

# Load DialoGPT
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

@app.route("/", methods=["GET", "POST"])
def chat():
    if "chat_history_ids" not in session:
        session["chat_history_ids"] = None
        session["history"] = []

    user_input = ""

    if request.method == "POST":
        user_input = request.form["user_input"]

        # Tokenize and update chat history
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        if session["chat_history_ids"] is not None:
            prev_ids = torch.tensor(session["chat_history_ids"], dtype=torch.long)
            bot_input_ids = torch.cat([prev_ids, new_input_ids], dim=-1)
        else:
            bot_input_ids = new_input_ids

        chat_history_ids = model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8
        )

        bot_response = tokenizer.decode(
            chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True
        )

        # Store in session
        session["chat_history_ids"] = chat_history_ids.tolist()
        session["history"].append({"role": "You", "text": user_input})
        session["history"].append({"role": "Bot", "text": bot_response})

        return redirect(url_for("chat"))

    return render_template("chat.html", history=session.get("history", []))

@app.route("/clear", methods=["POST"])
def clear():
    session.pop("chat_history_ids", None)
    session.pop("history", None)
    return redirect(url_for("chat"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)