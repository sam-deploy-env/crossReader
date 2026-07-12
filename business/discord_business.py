import time

from utils import word_generator, file_reader, category_init, rewards
from repositories.SettingRepository import SettingRepository
from repositories.RunnerRepository import RunnerRepository
from constants import messages, file_data
from mail_sender import mail_service

setting_repository = SettingRepository()
runner_repository = RunnerRepository()

async def mail(ctx):
    word_generator.create_word_file()
    mail_service.send_mail()
    await ctx.send(messages.MAIL_SEND)

async def delete(ctx):
    runner_repository.delete_all()
    await ctx.send(messages.DB_DELETE)

async def init(ctx):
    runner_repository.delete_all()
    setting_repository.set_number_scratch_m(3)
    setting_repository.set_number_scratch_f(3)
    setting_repository.set_mail_sent(0)
    setting_repository.set_started(0)
    category_init.init_categories()
    await ctx.send(messages.DB_INIT)

async def setmail(ctx, arg):
    if arg.lower() in ["on", "1"]:
        setting_repository.set_mail_sent(1)
        await ctx.send(messages.MAIL_ON)
    elif arg.lower() in ["off", "0"]:
        setting_repository.set_mail_sent(0)
        await ctx.send(messages.MAIL_OFF)
    else:
        await ctx.send(messages.MAIL_KO)

async def started(ctx, arg):
    if arg.lower() in ["on", "1"]:
        setting_repository.set_started(1)
        await ctx.send(messages.STARTED_ON)
    elif arg.lower() in ["off", "0"]:
        setting_repository.set_started(0)
        await ctx.send(messages.STARTED_OFF)
    else:
        await ctx.send(messages.STARTED_KO)

async def test(ctx):
    await ctx.send(messages.OK)

async def clear(ctx, nombre):
    await ctx.channel.purge(limit=nombre+1, check=lambda msg: not msg.pinned)

async def cmd(ctx):
    await ctx.send(messages.CMD)

async def import_file(message):
    file = await message.attachments[0].to_file()
    if not file.filename.endswith(".sbcap"):
        await message.channel.send(messages.UNKNOWN_EXTENSION)
        return
    await message.attachments[0].save(file_data.SBCAP_FILENAME)
    start = time.time()
    await file_reader.read_file(file_data.SBCAP_FILENAME)
    end = time.time()
    duration = round(end - start, 2)
    await message.channel.send(messages.FILE_TREATED + " en " + str(duration) + " secondes")
    rewards.update_rewards()
        