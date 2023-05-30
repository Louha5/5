from datetime import datetime
import vk_api
import sqlite3
from vk_api.longpoll import VkLongPoll, VkEventType

a = "vk1.a.B1PNMSJhyd8HUs6Qkg3mvqVsXQTBG9QPk4sc-e8t40xyJ2pJQIewRXR3a-rI3YAmV3sbL1Wz3Ole2HK1rpKw3IBvTWu4Q1s6DTAoVMEDxTEw0R59wBY-1OOv3nqUFJnw-DZp71GYzXGZnOUZfoCmV27P3FAUIZkgp3jfh1LQ9QoyrtmMYuLcjC13_YGtnXdH2SGVMbPXi_NFP4_LAOaUcQ"
b = "vk1.a.RehOSIygJLsUYB2qfTvellkZnJ52fsVuXMUcpVWazTvT8acp68EMXL7e2ovUQK4_rZUVz4kZEBgEWJ3dEigIsK6_DD6YU4sOrnkbSyqyBjP8mESNE5bJvjvGpWXK1bw7NwTubCX6F4fDskcuEh4ypAZLAy2oTbqaxLgWAkS2Fym5BqbPbH3x56cjjuON3iqPRjkAClcUb684xeB5IYLBnA"


class VKBot:
    soc = []
    link = []

    def __init__(self, bot_name, api_token):
        self.session = vk_api.VkApi(token=api_token)
        self.longpoll = VkLongPoll(self.session)
        self.vk = self.session.get_api()
        self.bot_name = bot_name
        self.conn = sqlite3.connect(self.bot_name + ".dp")

    def send_message(self, message, id):
        self.vk.messages.send(message=message, user_id=id, random_id=datetime.now().microsecond)

    def printik(self, arr):
        b1 = len(arr)
        z = ""
        for i in range(0,b1):
            z += str(arr[i][1]) + " " + str(arr[i][2]) + " " + str(arr[i][3]) + " кабинет" +"\n"
        return z

    def start(self):
        init_dp = open("init_db.sql")
        raw_init = init_dp.readlines()
        init = ""
        for line in raw_init:
            init += line.replace("\n"," ")
        self.conn.executescript(init)
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text.split(" ")[0] == self.bot_name:
                smsuser = event.text.split(" ")
                if smsuser[1] == "сохрани" and smsuser[2] == "фразу" and len(smsuser) > 3:
                    phrase = event.text[15 + len(self.bot_name):]
                    self.conn.execute(f'INSERT OR REPLACE INTO user_info(vk_id, sentence) VALUES ({event.user_id},"{phrase}")')
                    print(self.conn.execute("SELECT * FROM user_info").fetchall())
                    self.conn.commit()
                    self.send_message(f"Фраза {phrase} успешно сохранена",event.user_id)
                if len(smsuser) > 2 and smsuser[1] == "напиши" and smsuser[2] == "фразу":
                    answer = self.conn.execute(f"SELECT sentence FROM user_info WHERE vk_id = {event.user_id}").fetchall()
                    if len(answer) > 0:
                        print(answer)
                        self.send_message(f"Ваша фраза {answer[0][0]}", event.user_id)
                    else:
                        self.send_message("Вы не сохраняли фразу", event.user_id)
                if len(smsuser) > 4 and smsuser[1] == "добавь" and smsuser[2] == "соцсеть":
                    social = event.text[16 + len(self.bot_name):]
                    socialnet = social.split("; ")
                    for i in range(len(socialnet)):
                        VKBot.soc.append(socialnet[i].split(": ")[0])
                        VKBot.link.append(socialnet[i].split(": ")[1])
                    self.conn.execute(f'INSERT OR REPLACE INTO user_social_network(vk_id, social, link) VALUES ({event.user_id},"{VKBot.soc}","{VKBot.link}")')
                    self.conn.commit()
                    print(self.conn.execute("SELECT * FROM user_social_network").fetchall())
                if len(smsuser) > 1 and smsuser[1] == "приветствие":
                    self.send_message("Здравствуйте! Вас приветствует вкбот Яжбот", event.user_id)
                if len(smsuser) == 2 and smsuser[1] == "расписание":
                    monday = self.conn.execute(f"SELECT * FROM user_Monday WHERE vk_id = {event.user_id}").fetchall()
                    tuesday = self.conn.execute(f"SELECT * FROM user_Tuesday WHERE vk_id = {event.user_id}").fetchall()
                    wednesday = self.conn.execute(f"SELECT * FROM user_Wednesday WHERE vk_id = {event.user_id}").fetchall()
                    thursday = self.conn.execute(f"SELECT * FROM user_Thursday WHERE vk_id = {event.user_id}").fetchall()
                    friday = self.conn.execute(f"SELECT * FROM user_Friday WHERE vk_id = {event.user_id}").fetchall()
                    saturday = self.conn.execute(f"SELECT * FROM user_Saturday WHERE vk_id = {event.user_id}").fetchall()
                    sunday = self.conn.execute(f"SELECT * FROM user_Sunday WHERE vk_id = {event.user_id}").fetchall()
                    self.send_message(str("Понедельник:"+self.printik(monday)+"\nВторник:"+self.printik(tuesday)+"\nСреда:"+self.printik(wednesday)+"\nЧетверг:"+self.printik(thursday)+"\nПятница:"+self.printik(friday)+"\nСуббота:"+self.printik(saturday)+"\nВоскресение:"+self.printik(sunday)), event.user_id)
                if len(smsuser) > 2 and smsuser[1] == "расписание":
                    monday = self.conn.execute(f"SELECT * FROM user_Monday WHERE vk_id = {event.user_id}").fetchall()
                    tuesday = self.conn.execute(f"SELECT * FROM user_Tuesday WHERE vk_id = {event.user_id}").fetchall()
                    wednesday = self.conn.execute(f"SELECT * FROM user_Wednesday WHERE vk_id = {event.user_id}").fetchall()
                    thursday = self.conn.execute(f"SELECT * FROM user_Thursday WHERE vk_id = {event.user_id}").fetchall()
                    friday = self.conn.execute(f"SELECT * FROM user_Friday WHERE vk_id = {event.user_id}").fetchall()
                    saturday = self.conn.execute(f"SELECT * FROM user_Saturday WHERE vk_id = {event.user_id}").fetchall()
                    sunday = self.conn.execute(f"SELECT * FROM user_Sunday WHERE vk_id = {event.user_id}").fetchall()
                    day = smsuser[2]
                    if day == "понедельник":
                        b1 = len(monday)
                        self.send_message(self.printik(monday), event.user_id)
                    elif day == "вторник":
                        self.send_message(self.printik(tuesday), event.user_id)
                    elif day == "среда":
                        self.send_message(self.printik(wednesday), event.user_id)
                    elif day == "четверг":
                        self.send_message(self.printik(thursday), event.user_id)
                    elif day == "пятница":
                        self.send_message(self.printik(friday), event.user_id)
                    elif day == "суббота":
                        self.send_message(self.printik(saturday), event.user_id)
                    elif day == "воскресение":
                        self.send_message(self.printik(sunday), event.user_id)
                if len(smsuser) > 6 and smsuser[1] == "добавь" and smsuser[2] == "предмет":
                    try:
                        integer = smsuser[4].split(":")
                        a1 = int(integer[0])
                        a2 = int(integer[1])
                        if 0<= a1 < 24 and 0<= a2 < 60:
                            day = smsuser[3]
                            if day == "понедельник":
                                self.conn.execute(
                                    f'INSERT OR REPLACE INTO user_Monday(vk_id, time , name_lesson, office) VALUES ({event.user_id},"{smsuser[4]}","{smsuser[5]}","{smsuser[6]}")')
                                self.conn.commit()
                            elif day == "вторник":
                                self.conn.execute(
                                    f'INSERT OR REPLACE INTO user_Tuesday(vk_id, time , name_lesson, office) VALUES ({event.user_id},"{smsuser[4]}","{smsuser[5]}","{smsuser[6]}")')
                                self.conn.commit()
                            elif day == "среда":
                                self.conn.execute(
                                    f'INSERT OR REPLACE INTO user_Wednesday(vk_id, time , name_lesson, office) VALUES ({event.user_id},"{smsuser[4]}","{smsuser[5]}","{smsuser[6]}")')
                                self.conn.commit()
                            elif day == "четверг":
                                self.conn.execute(
                                    f'INSERT OR REPLACE INTO user_Thursday(vk_id, time , name_lesson, office) VALUES ({event.user_id},"{smsuser[4]}","{smsuser[5]}","{smsuser[6]}")')
                                self.conn.commit()
                            elif day == "пятница":
                                self.conn.execute(
                                    f'INSERT OR REPLACE INTO user_Friday(vk_id, time , name_lesson, office) VALUES ({event.user_id},"{smsuser[4]}","{smsuser[5]}","{smsuser[6]}")')
                                self.conn.commit()
                            elif day == "суббота":
                                self.conn.execute(
                                    f'INSERT OR REPLACE INTO user_Saturday(vk_id, time , name_lesson, office) VALUES ({event.user_id},"{smsuser[4]}","{smsuser[5]}","{smsuser[6]}")')
                                self.conn.commit()
                            elif day == "воскресение":
                                self.conn.execute(
                                    f'INSERT OR REPLACE INTO user_Sunday(vk_id, time , name_lesson, office) VALUES ({event.user_id},"{smsuser[4]}","{smsuser[5]}","{smsuser[6]}")')
                                self.conn.commit()
                            self.send_message("Добавление прошло успешно", event.user_id)
                        else:
                            self.send_message("Неправельное время", event.user_id)
                    except ValueError:
                        self.send_message("Неверное время", event.user_id)
                if len(smsuser) > 6 and smsuser[1] == "удали" and smsuser[2] == "предмет":
                    try:
                        integer = smsuser[4].split(":")
                        a1 = int(integer[0])
                        a2 = int(integer[1])
                        if 0 <= a1 < 24 and 0 <= a2 < 60:
                            day = smsuser[3]
                            if day == "понедельник":
                                self.conn.execute(
                                    f'DELETE FROM user_Monday WHERE vk_id = {event.user_id} AND time = "{smsuser[4]}"')
                                self.conn.commit()
                            elif day == "вторник":
                                self.conn.execute(
                                    f'DELETE FROM user_Tuesday WHERE vk_id = {event.user_id} AND time = "{smsuser[4]}"')
                                self.conn.commit()
                            elif day == "среда":
                                self.conn.execute(
                                    f'DELETE FROM user_Wednesday WHERE vk_id = {event.user_id} AND time = "{smsuser[4]}"')
                                self.conn.commit()
                            elif day == "четверг":
                                self.conn.execute(
                                    f'DELETE FROM user_Thursday WHERE vk_id = {event.user_id} AND time = "{smsuser[4]}"')
                                self.conn.commit()
                            elif day == "пятница":
                                self.conn.execute(
                                    f'DELETE FROM user_Friday WHERE vk_id = {event.user_id} AND time = "{smsuser[4]}"')
                                self.conn.commit()
                            elif day == "суббота":
                                self.conn.execute(
                                    f'DELETE FROM user_Saturday WHERE vk_id = {event.user_id} AND time = "{smsuser[4]}"')
                                self.conn.commit()
                            elif day == "воскресение":
                                self.conn.execute(
                                    f'DELETE FROM user_Sunday WHERE vk_id = {event.user_id} AND time = "{smsuser[4]}"')
                                self.conn.commit()
                            self.send_message("Удаление прошло успешно", event.user_id)
                    except ValueError:
                        self.send_message("Неверное время", event.user_id)


bot = VKBot("Яжбот", b)
bot.start()
