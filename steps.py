from telegram import Update
from telegram.ext import CallbackContext
from database import SessionLocal, UserSteps

async def add_steps(update: Update, context: CallbackContext):
    session = SessionLocal()
    user_id = update.message.from_user.id
    steps = int(context.args[0]) if context.args else 0

    user = session.query(UserSteps).filter_by(user_id=user_id).first()
    if not user:
        user = UserSteps(user_id=user_id, steps=0)
        session.add(user)

    user.steps += steps
    session.commit()
    session.close()

    await update.message.reply_text(f"Добавлено {steps} шагов. Всего: {user.steps} шагов.")
    