import asyncio
import json
from itertools import dropwhile
from helper.account_handler import add_member
from init import rs, w, r, banner, clr
from pyrogram.errors import FloodWait  # Jika Anda menggunakan Pyrogram untuk Telegram API
import time

clr()
banner()
print(f"  {r}Version: {w}3.1 {r}| Author: {w}SAIF ALI{rs}\n")
print(f"  {r}Telegram {w}@DearSaif {r}| Instagram: {w}@_Prince.Babu_{rs}\n")

# option for choose username or id
option = input("choose method username or id: ").lower()


async def main():
    # loads member
    try:
        user_id = json.load(open("data/user.json", encoding="utf-8"))
    except:
        user_id = json.load(open("data/source_user.json", encoding="utf-8"))

    # loads users and channel info
    config = json.load(open("config.json", encoding="utf-8"))

    # list to chcek active member
    activelist = [
        "UserStatus.RECENTLY",
        "UserStatus.LAST_MONTH",
        "UserStatus.LAST_WEEK",
        "UserStatus.OFFLINE",
        "UserStatus.RECENTLY",
        "UserStatus.ONLINE",
    ]
    
    # count retrive old state
    last_active = config["from_date_active"]
    added = 0
    active = []

    for x in dropwhile(lambda y: y != last_active, activelist):
        active.append(x)
    
    for user in user_id:
        try:
            await add_member(user, config, active, option)
            added += 1
            # Tambahkan jeda 2-5 detik untuk menghindari floodwait atau spam
            await asyncio.sleep(2)  # Bisa disesuaikan dengan delay yang lebih lama jika masih kena floodwait

        except FloodWait as e:
            print(f"Floodwait terjadi, menunggu selama {e.x} detik...")
            await asyncio.sleep(e.x)  # Menunggu waktu floodwait
        except Exception as err:
            print(f"Terjadi error: {err}")
    
    print(f"Total members added: {added}")


asyncio.run(main())
