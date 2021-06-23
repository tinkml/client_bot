import aiogram.utils.markdown as md


def get_welcome_message_chat_text(data: dict) -> str:
    return md.text(
            md.text('Hi! Nice to meet you,', md.bold(data['name'])),
            md.text('Age:', md.code(data['age'])),
            md.text('Gender:', data['gender']),
            sep='\n',
        )
