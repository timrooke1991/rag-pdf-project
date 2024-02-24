from langchain.chat_models import ChatOpenAI


def build_llm(chat_args, model_name):
    return ChatOpenAI(
        streaming=chat_args.streaming,
        model_name=model_name,
    )

# # Usage:
# builder = build_llm("gpt-4")
# builder(chat_args) # chat_args is a dict with the chat arguments