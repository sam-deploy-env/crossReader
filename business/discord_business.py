import asyncio
import time

from repositories.SettingRepository import SettingRepository
from utils import word_generator, file_reader, category_init, rewards
from repositories.CategoryRepository import CategoryRepository
from repositories.RunnerRepository import RunnerRepository
from constants import messages, file_data
from mail_sender import mail_service
from database import SessionLocal


async def mail(ctx):
    session = SessionLocal()
    try:
        category_repo = CategoryRepository(session)
        runner_repo = RunnerRepository(session)
        word_generator.create_word_file(category_repo, runner_repo)
        mail_service.send_mail()
        await ctx.send(messages.MAIL_SEND)
    finally:
        session.close()

async def delete(ctx):
    session = SessionLocal()
    try:
        runner_repo = RunnerRepository(session)
        runner_repo.delete_all()
        await ctx.send(messages.DB_DELETE)
    finally:
        session.close()

async def init(ctx):
    session = SessionLocal()
    try:
        category_repo = CategoryRepository(session)
        runner_repo = RunnerRepository(session)
        setting_repo = SettingRepository(session)
        runner_repo.delete_all()
        setting_repo.set_number_scratch_m(3)
        setting_repo.set_number_scratch_f(3)
        setting_repo.set_mail_sent(0)
        setting_repo.set_started(0)
        category_init.init_categories(category_repo, setting_repo)
        await ctx.send(messages.DB_INIT)
    finally:
        session.close()

async def setmail(ctx, arg):
    session = SessionLocal()
    try:
        setting_repo = SettingRepository(session)
        if arg.lower() in ["on", "1"]:
            setting_repo.set_mail_sent(1)
            await ctx.send(messages.MAIL_ON)
        elif arg.lower() in ["off", "0"]:
            setting_repo.set_mail_sent(0)
            await ctx.send(messages.MAIL_OFF)
        else:
            await ctx.send(messages.MAIL_KO)
    finally:
        session.close()

async def started(ctx, arg):
    session = SessionLocal()
    try:
        setting_repo = SettingRepository(session)
        if arg.lower() in ["on", "1"]:
            setting_repo.set_started(1)
            await ctx.send(messages.STARTED_ON)
        elif arg.lower() in ["off", "0"]:
            setting_repo.set_started(0)
            await ctx.send(messages.STARTED_OFF)
        else:
            await ctx.send(messages.STARTED_KO)
    finally:
        session.close()

async def test(ctx):
    await ctx.send(messages.OK)

async def clear(ctx, nombre):
    await ctx.channel.purge(limit=nombre+1, check=lambda msg: not msg.pinned)

async def cmd(ctx):
    await ctx.send(messages.CMD)

async def import_file(message):
    session = SessionLocal()
    try:
        runner_repo = RunnerRepository(session)
        file = await message.attachments[0].to_file()
        if not file.filename.endswith(".sbcap"):
            await message.channel.send(messages.UNKNOWN_EXTENSION)
            return
        await message.attachments[0].save(file_data.SBCAP_FILENAME)
        start = time.time()
        await file_reader.read_file(runner_repo, file_data.SBCAP_FILENAME)
        end = time.time()
        duration = round(end - start, 2)
        await message.channel.send(messages.FILE_TREATED + " en " + str(duration) + " secondes")
        await asyncio.to_thread(rewards.update_rewards)
    finally:
        session.close()
        