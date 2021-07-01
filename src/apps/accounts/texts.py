from enum import Enum


class SignUpTexts(Enum):

    canceled = 'Сценарий отменен'
    start_sign_up = 'Начало регистрации.\n' \
                    'Ваше имя и фамилия: {first_name} {last_name}.\n' \
                    'Подтвердите указанное Имя и Фамилию, либо напишите другие.'
    fullname_confirmation = 'Это мои Имя и Фамилия'
    is_user_a_legal_entity = "Вы Юр.лицо, либо ИП?"
    is_legal_entity_incorrect_answer = "Не корректное значение. Вы Юр. лицо, либо ИП? " \
                                       "(Выберите одни из предложенных значений)"
    sign_up_is_over = 'Регистрация закончена.'
