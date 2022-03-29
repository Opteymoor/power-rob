from requests import get
from re import findall
from rubika.client import Bot
from requests import post
import time
from PIL import Image
from json import loads
from gtts import gTTS
from mutagen.mp3 import MP3
import io

bot = Bot("AppName", auth=)
target ="g0BNopQ0cac9a1adfe570cad15f513c5"
bot.sendMessage(target, 'اپراتور ددپول فعال شده🤖✅')
def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me"]
	for i in links:
		if i in msg:
			return True
	

# static variable
answered, sleeped, retries = [], False, {}

alerts, blacklist = [] , []

def alert(guid,user,link=False):
	alerts.append(guid)
	coun = int(alerts.count(guid))

	haslink = ""
	if link : haslink = "گزاشتن لینک در گروه ممنوع میباشد .\n\n"

	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما (1/3) اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما (2/3) اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")

	elif coun == 3:
		blacklist.append(guid)
		bot.sendMessage(target, "🚫 کاربر [ @"+user+" ] \n (3/3) اخطار دریافت کرد ، بنابراین اکنون کوبنت را پاره میکنم.")
		bot.banGroupMember(target, guid)

retries = {}
sleeped = False
 
plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "/bot" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "The bot is now active", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بیو") or msg.get("text").startswith("bio") or msg.get("text").startswith("!bio"):
						
						try:
							response = get("https://api.codebazan.ir/bio").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("دانش") or msg.get("text").startswith("danestani") or msg.get("text").startswith("!danestani"):
						
						try:
							response = get("https://api.codebazan.ir/danestani/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("الکی") or msg.get("text").startswith("alaki-masalan") or msg.get("text").startswith("!alaki-masalan"):
						
						try:
							response = get("https://api.codebazan.ir/jok/alaki-masalan/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("دانستنی") or msg.get("text").startswith("dastan") or msg.get("text").startswith("!dastan"):
						
						try:
							response = get("https://api.codebazan.ir/dastan/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("ذکر") or msg.get("text").startswith("zekr") or msg.get("text").startswith("!zekr"):
						
						try:
							response = get("http://api.codebazan.ir/zekr/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("خاطره") or msg.get("text").startswith("khatere") or msg.get("text").startswith("!khatere"):
						
						try:
							response = get("http://api.codebazan.ir/jok/khatere").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور رابه طورصحیح وارد کنید❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("پ ن پ") or msg.get("text").startswith("pa-na-pa") or msg.get("text").startswith("!pa-na-pa"):
						
						try:
							response = get("http://api.codebazan.ir/jok/pa-na-pa/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
							
					
					
							
					
						
					elif msg.get("text").startswith("صکص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کیری"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بیناموص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بی ناموص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بیناموس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بی ناموس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کسکش"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کوبص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کبص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کوس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کیرم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادرتو"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادرت"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کون"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کوس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کونی"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("جنده"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("جند"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادر جنده"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادر جند"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("ممه"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("kir"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("https://"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام تبلیغاتی پاک شد", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("گایید"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نگایدم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("گایدی"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نگاید"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نگایدیم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("گایدیم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کیر"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					
						
					elif msg.get("text").startswith("کص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("لاشی"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("دیوث"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("غیر فعال ارام") and msg.get("author_object_guid") in admins:
							try:
								number = 0
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						
					elif msg.get("text").startswith("ارام10") and msg.get("author_object_guid") in admins:
							try:
								number = 10
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("ارام1") and msg.get("author_object_guid") in admins:
							try:
								number = 60
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("ارام5") and msg.get("author_object_guid") in admins:
							try:
								number = 300
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))															
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("ارام15") and msg.get("author_object_guid") in admins:
							try:
								number = 900
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("ارام1s") and msg.get("author_object_guid") in admins:
							try:
								number = 1600
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("ارام30") and msg.get("author_object_guid") in admins:
							try:
								number = 30
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "!speak" or msg.get("text") == "speak" or msg.get("text") == "Speak" or msg.get("text") == "بگو":
							try:
								if msg.get('reply_to_message_id') != None:
									msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if msg_reply_info['text'] != None:
										text = msg_reply_info['text']
										speech = gTTS(text)
										changed_voice = io.BytesIO()
										speech.write_to_fp(changed_voice)
										b2 = changed_voice.getvalue()
										changed_voice.seek(0)
										audio = MP3(changed_voice)
										dur = audio.info.length
										dur = dur * 1000
										f = open('sound.ogg','wb')
										f.write(b2)
										f.close()
										bot.sendVoice(target , 'sound.ogg', dur,message_id=msg["message_id"])
										os.remove('sound.ogg')
										print('sended voice')
								else:
									bot.sendMessage(target, 'پیام شما متن یا کپشن ندارد',message_id=msg["message_id"])
							except:
								print('server gtts bug')		
					
																			
				
					elif msg.get("text") == "سنجاق" and msg.get("author_object_guid") in admins :
							try:
								bot.pin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر با موفقیت سنجاق شد!", message_id=msg.get("message_id"))
							except:
								print("err pin")
								
					elif msg["text"].startswith("!number") or msg["text"].startswith("بشمار"):
							try:
								response = get(f"http://api.codebazan.ir/adad/?text={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])				
								
					elif msg.get("text").startswith("حدیث") or msg.get("text").startswith("hadis") or msg.get("text").startswith("!hadis"):
							try:
								response = get("http://api.codebazan.ir/hadis/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "ببخشید، خطایی تو ارسال پیش اومد!", message_id=msg["message_id"])
								
					elif msg.get("text").startswith("دیالوک") or msg.get("text").startswith("dialog") or msg.get("text").startswith("!dialog"):
							try:
								response = get("http://api.codebazan.ir/dialog/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "متاسفانه تو ارسال مشکلی پیش اومد!", message_id=msg["message_id"])
								
					elif msg.get("text").startswith("داستان") or msg.get("text").startswith("!dastan"):
							try:
								response = get("http://api.codebazan.ir/dastan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "مشکلی پیش اومد!", message_id=msg["message_id"])	
								
					elif msg.get("text") == "دستورات":
							rules = open("dast.txt","r",encoding='utf-8').read()
							bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("اپدیت دستورات") and msg.get("author_object_guid") in admins:
							try:
								rules = open("dast.txt","w",encoding='utf-8').write(str(msg.get("text").strip("اپدیت دستورات")))
								bot.sendMessage(target, "دستورات با موفقیت بروزرسانی شد.", message_id=msg.get("message_id"))
								
							except:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید.", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("بازی") or msg.get("text").startswith("جرعت حقیقت") or msg.get("text").startswith("ج ح"):
							rules = open("jorat.txt","r",encoding='utf-8').read()
							bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("اپدیت بازی") and msg.get("author_object_guid") in admins:
							try:
								rules = open("jorat.txt","w",encoding='utf-8').write(str(msg.get("text").strip("اپدیت بازی")))
								bot.sendMessage(target, "بازی با موفقیت بروزرسانی شد.", message_id=msg.get("message_id"))
								
							except:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید.", message_id=msg.get("message_id"))			
								
					elif msg.get("text").startswith("اب وهوا") or msg.get("text").startswith("weather") or msg.get("text").startswith("!weather"):
						try:
							city = msg.get('text').split()[1]
							jd = loads(get('https://api.codebazan.ir/weather/?city=' + city).text)
							text = 'دما : \n'+jd['result']['دما'] + '\n سرعت باد:\n' + jd['result']['سرعت باد'] + '\n وضعیت هوا: \n' + jd['result']['وضعیت هوا'] + '\n\n بروز رسانی اطلاعات امروز: ' + jd['result']['به روز رسانی'] + '\n\nپیش بینی هوا فردا: \n  دما: ' + jd['فردا']['دما'] + '\n  وضعیت هوا : ' + jd['فردا']['وضعیت هوا']
							bot.sendMessage(target, text , message_id=msg["message_id"])
						except:
							print('code bz weather err')
							bot.sendMessage(target, 'متاسفانه سرور ارور داد' , message_id=msg["message_id"])	
								
					elif msg.get("text").startswith("مدیر کیه") or msg.get("text").startswith("مدیران") or msg.get("text").startswith("لیست مدیران"):
							rules = open("aa.txt","r",encoding='utf-8').read()
							bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("اپدیت مدیران") and msg.get("author_object_guid") in admins:
							try:
								rules = open("aa.txt","w",encoding='utf-8').write(str(msg.get("text").strip("اپدیت مدیران")))
								bot.sendMessage(target, "لیست مدیران با موفقیت بروزرسانی شد.", message_id=msg.get("message_id"))
								
							except:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید.", message_id=msg.get("message_id"))		
								
					elif msg.get("text").startswith("wrt"):
						try:
							data = msg.get("text").split("\n")
							f = open("data.txt","a",encoding="utf")
							f.write(str(data[1] + "|=|" + data[2] + "|/|" + "\n" ))
							f.close()
							bot.sendMessage(target, "آها یاد گرفتم✅", message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستورات را درست وارد کنید ❌", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("کمک") or msg.get("text").startswith("/help") or msg.get("text").startswith("!help"):
							try:
								bot.sendMessage(msg.get("author_object_guid"), "دستورات ددپول دستورات ددپول بات✅🤖 \n ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖ \nبرای کاربران گرارمی👌 \n1ـ 😁جوک \n2ـ😉فونت(فونت شاخ) \n3ـ😃دانستی \n4ـ💠 ماشین حساب (حساب) \n5ـ🔮 بیوگرافی \n6ـ📿ذکر  \n7ـ👨‍🎓سوال دانشی(دانشی) \n8ـ🤡 پ ن پ \n9ـ 😻 خاطره \n10ـ👻 الکی مثلا \n11ـ📃 ترجمه ( مترجم) \n12ـ💌 ارسال پیام به پیوی (پیام) \n13ـ👨‍👨‍👦‍👦 ادد ( افزودن کار بر با ایدی) \n14ـ📖 قوانین(قوانین گروه) \n15ـ⏰ تایم (ساعت) \n16ـ📆تاریخ \n17-🗣دادن ویس(بگو) \n18-📜ارسال حدیث \n19-✅دادن یک عدد وترجمه کردن ان عدد \n20-🗂داستان \n21-📙دیالوگ \n22-🔫لیست بازی ج \n23-⛈اب وهوا \n 24-📸شات از متن(شات) \n25-📹عکس جستجو (عکس جستجو)\n26-💡جستجو(جستجو) \n27-😎نام شاخ(نام شاخ) \n28-🗿یادگیر کلمات مثال \nwrt \nحرفه شما \nجواب ربات\n〰〰〰〰〰〰〰〰〰〰〰〰〰〰 \n توجه🤵( داشتی باشد اگه ادمین نت نداشته باشن قابلیت در دست رس نیست🤦‍♂) \n➰➰➰➰➰➰➰➰➰➰➰➰➰➰\n👮‍♂برای ادمین ها👩‍💻 \n1ـ🚫 اخطار(3)بشه ریم \n 2ـ❎گپ بسته (گپ سته میشه) \n3ـ✅گپ باز(گپ باز میشه) \n 4ـ❌ ریم (کار بر حذف میشه) \n5ـ📝 حذف(حذف پیام)باریپ رویه ان \n 6ـ💬 ارام (گروه 10ثانیه میره رو حالت ارام) \n7ـ🗯 غیر فعال ارام (غیر فعال کردن حالت ارام) \n8ـ☣روشن (روشن کردن آذرخش) \n9ـ📴 خاموش (خاموش کردن زئوس)\n10-🎙سنجاق پیام(سنجاق) \n ۱۱-🧠اموزش هوش مصنوعی اول کلمه(wet)رابزنید بعدمتن خودرا بگید بعد جواب زیر متن \n➿➿➿➿➿➿➿➿➿➿➿➿➿➿ \nتوجه😄(ربات داری قابلیت حذف فوش وحذف لینک میباشد پس لینک و فوش ندهید چت خوش😘❤️))").text
								bot.sendMessage(target, "نتیجه کامل به پیوی شما ارسال شد✔️", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "نتیجه کامل به پیوی شما ارسال شد✔️", message_id=msg["message_id"])
								
					elif msg.get("text").startswith("شات") or msg.get("text").startswith("!shot") or msg.get("text").startswith("shot"):
						if msg.get('reply_to_message_id') != None:
							msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
							if msg_reply_info['text'] != None:
								text = msg_reply_info['text']
								res = get('https://api.otherapi.tk/carbon?type=create&code=' + text + '&theme=vscode')
								if res.status_code == 200 and res.content != b'':
									b2 = res.content
									print('get the image')
									f = open('image.jpg','wb')
									f.write(b2)
									f.close()
									p = Image.open('image.jpg')
									bot.sendPhoto(target, 'image.jpg', p.size,message_id=msg["message_id"])
								else:
									bot.sendMessage(target, 'ارتباط با سرور ناموفق',message_id=msg["message_id"])
							else:
								bot.sendMessage(target, 'پیام شما متن یا کپشن ندارد',message_id=msg["message_id"])
				
						else:
							bot.sendMessage(target, 'لطفا روی یک پیام ریپلای بزنید',message_id=msg["message_id"])
							
					elif msg.get("text").startswith("عکس جستجو") or msg.get("text").startswith("webshot") or msg.get("text").startswith("!webshot"):
						
						try:
							args = msg['text'].split()[1]
							if '.ir' in args:
								response = get(f"https://api.codebazan.ir/webshot/?text=1000&domain={args}").content
							else:
								response = get("https://http.cat/403").content
							with open("shot.jpg","wb") as shot: shot.write(response)
							bot.sendPhoto(target, "./shot.jpg", [720,720], caption="نمایی از صفحه موردنظر شما", message_id=msg["message_id"])
						except: bot.sendMessage(target, "متأسفانه نتیجه‌ای در بر نداشت ☹️", message_id=msg["message_id"])
					
					elif msg.get("text") == "حذف" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام پاک شد ✅", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نام شاخ"):
						
						try:
							response = get("https://api.codebazan.ir/name/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])
						
					elif msg.get("text"):
						mop = open("data.txt","r",encoding="utf")
						ooo = mop.read().split("|/|")
						for i in ooo:
							ii = i.split("|=|")
							if msg.get("text") in ii[0]:
								bot.sendMessage(target, ii[1], message_id=msg["message_id"])
						mop.close()
					elif msg.get("text").startswith("wrt"):
						try:
							data = msg.get("text").split("\n")
							f = open("data.txt","a",encoding="utf")
							f.write(str(data[1] + "|=|" + data[2] + "|/|" + "\n" ))
							f.close()
							bot.sendMessage(target, "جیگرت دراد یاد گرفتم ✅", message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستورات را درست وارد کنید ❌", message_id=msg.get("message_id"))
					
					elif msg["text"] == "لینک":
								try:
									group = bot.getGroupLink(target)["data"]["join_link"]
									bot.sendMessage(target, "🔗 لینک گروه :\n"+str(group), msg["message_id"])
								except:
									print('err send link')
									
							
							
					elif msg.get("text").startswith("جستجو") or msg.get("text").startswith("!search") or msg.get("text").startswith("search"):
						try:
							search = msg.get('text').split()[1]                             
							jd = loads(get('https://zarebin.ir/api/?q=' + search + '&page=1&limit=10').text)
							results = jd['results']['webs']
							text = ''
							for result in results:
								text += result['title'] + ':\n\n  ' + str(result['description']).replace('</em>', '').replace('<em>', '').replace('(Meta Search Engine)', '').replace('&quot;', '').replace(' — ', '').replace(' AP', '') + '\n\n'
							bot.sendMessage(target, 'نتایج کامل به پیوی شما ارسال شد', message_id=msg["message_id"])
							bot.sendMessage(msg['author_object_guid'], 'نتایج یافت شده برای (' + search + ') : \n\n'+text)
						except:
							print('zarebin search err')	
							
				
				
					
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																		

					if msg.get("text") == "/بات" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "ربات در حال اضر فعال است", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("ادد") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "کاربر به گپ اضافه شد ✅", message_id=msg.get("message_id"))

					

					elif msg.get("text").startswith("ماشین حساب") or msg.get("text").startswith("حساب") or msg.get("text").startswith("حساب کن"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("دعوت ") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "https://rubika.ir/joing/CBBAGJFB0NYDVKGTZRDVMRSPHQKSLFRM\nسلام کاربر گرامی شما به گروه ما دعوت شدید❤️☘\nراستی قوانین گپ را رعایت کن✅\nفحش=ریمو❌\nناسزاگویی=ریمو❌\nشاخ=ریمو❌\nاسپم=ریمو❌\nکد هنگی=ریمو❌\nممنون میشیم وارد گروهمون شوید❤️\nعشــــــــــــــــــــــــــــــــــــــقی❤️💐"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "‌‌د‌عوت نامه شما با موفقیت ارسال گشت.", message_id=msg.get("message_id"))
					elif msg.get("text").startswith("پیام ") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "پیام ارسال شد ✅", message_id=msg.get("message_id"))
					

					elif msg.get("text") == "سلام":
						bot.sendMessage(target, "سلام عزیز", message_id=msg.get("message_id"))
						
					
												
					elif msg.get("text") == "خوبید" and msg.get("author_object_guid") :
												bot.sendMessage(target, "مرسی ماخوبیم توخوبی", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "سلاپ" and msg.get("author_object_guid") :
												bot.sendMessage(target, "سلاپ داپ🗿", message_id=msg.get("message_id"))
												
					elif msg.get("text").startswith("نخوندم"): 
							try:
								bot.sendMessage(target, "چون سواد نداری😜", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")
												
					elif msg.get("text") == "عه" and msg.get("author_object_guid") :
												bot.sendMessage(target, "اره", message_id=msg.get("message_id"))
												
					elif msg.get("text").startswith("نوب"): 
							try:
								bot.sendMessage(target, "پلیر😝", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")						
																		
					elif msg.get("text") == "خوبین" and msg.get("author_object_guid") :
												bot.sendMessage(target, "عالی😜", message_id=msg.get("message_id"))
												
					
						
					elif msg.get("text") == "رباط":
						bot.sendMessage(target, "جونم😁", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "باط":
						bot.sendMessage(target, "درست صدام کن (◔‿◔) ", message_id=msg.get("message_id"))
						
					
						
					elif msg.get("text") == "ممنون":
						bot.sendMessage(target, "عزیزی", message_id=msg.get("message_id"))
						
					
												
					elif msg.get("text") == "خبی":
						bot.sendMessage(target, "مرسی تو خبی🙃", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("هلیکوپتر") :
						bot.sendMessage(target, "▂▄▄▓▄▄▂\n◢◤ █▀▀████▄▄▄◢◤╬\n█▄ ██▄ ███▀▀▀▀▀▀\n◥█████◤\n══╩══╩═\nاینم از هلیکوپتر😅", message_id=msg.get("message_id"))
					
					
					elif msg.get("text").startswith("آیه_الکرسی") :
						bot.sendMessage(target, "ب‍‌ِس‍‌م‍ِ اللهِ ال‍‌رَّح‍‌م‍‌ن ال‍‌رَّح‍‌ی‍‌م‍ِ\n\nاللّهُ لاَ إِلَهَ إِلاَّ هُوَ الْحَیُّ الْقَیُّومُ لاَ تَأْخُذُهُ سِنَهٌ وَ لاَ نَوْمٌ لَّهُ مَا فِی السَّمَاوَاتِ وَمَا فِی الأَرْضِ مَن ذَا الَّذِی یَشْفَعُ عِنْدَهُ إِلاَّ بِإِذْنِهِ یَعْلَمُ مَا بَیْنَ أَیْدِیهِمْ وَمَا خَلْفَهُمْ وَ لاَ یُحِیطُونَ بِشَیْءٍ مِّنْ عِلْمِهِ إِلاَّ بِمَا شَاء وَسِعَ کُرْسِیُّهُ السَّمَاوَاتِ وَ الأَرْضَ وَ لاَ یَۆُودُهُ حِفْظُهُمَا وَ هُوَ الْعَلِیُّ الْعَظِیمُ لاَ إِکْرَاهَ فِی الدِّینِ قَد تَّبَیَّنَ الرُّشْدُ مِنَ الْغَیِّ فَمَنْ یَکْفُرْ بِالطَّاغُوتِ وَ یُۆْمِن بِاللّهِ فَقَدِ اسْتَمْسَکَ بِالْعُرْوَهِ الْوُثْقَیَ لاَ انفِصَامَ لَهَا وَاللّهُ سَمِیعٌ عَلِیمٌ اللّهُ وَلِیُّ الَّذِینَ آمَنُواْ یُخْرِجُهُم مِّنَ الظُّلُمَاتِ إِلَی النُّوُرِ وَالَّذِینَ کَفَرُواْ أَوْلِیَآۆُهُمُ الطَّاغُوتُ یُخْرِجُونَهُم مِّنَ النُّورِ إِلَی الظُّلُمَاتِ أُوْلَئِکَ أَصْحَابُ النَّارِ هُمْ فِیهَا خَالِدُونَ.\n\n#آیة_الکرسی | #قرآن", message_id=msg.get("message_id"))		
			 																																												
					

					elif msg.get("text") == "خاموش" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "ربات خاموش شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("پینگ"):
						
						try:
							responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							bot.sendMessage(target, responser,message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("اخطار") and msg.get("author_object_guid") in admins:
							try:
								user = msg.get("text").split(" ")[1][1:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									alert(guid,user)
									
								else :
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
									
							except IndexError:
								guid = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								if not guid in admins:
									alert(guid,user)
								else:
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "قوانین":
							rules = open("rules.txt","r",encoding='utf-8').read()
							bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("اپدیت قوانین") and msg.get("author_object_guid") in admins:
							try:
								rules = open("rules.txt","w",encoding='utf-8').write(str(msg.get("text").strip("اپدیت قوانین")))
								bot.sendMessage(target, "✅  قوانین بروزرسانی شد", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg["text"].startswith("امتیاز") or msg["text"].startswith("/star"):
								try:
									user = msg["text"].replace("امتیاز ","").replace("/star ","")[1:]
									guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
									star(guid,user)
									
								except:
									try:
										guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
										user = bot.getUserInfo(guid)["data"]["user"]["username"]
										star(guid,user)
									except:
										bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
			
						
							
					
					elif msg.get("text").startswith("ترجمه"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text").startswith("فونت"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							
					elif msg.get("text") == "خوبی" and msg.get("author_object_guid") :
												bot.sendMessage(target, "خوبم توخوفی", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "مرسی" and msg.get("author_object_guid") :
												bot.sendMessage(target, "بهش برسی🙂", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "صلام" and msg.get("author_object_guid") :
												bot.sendMessage(target, "صلام گل🥺🌹", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "اصل" and msg.get("author_object_guid") :
												bot.sendMessage(target, "ℤ𝕖𝕦𝕤𝔹𝕠𝕥 ¦ زئوس‌بات هستم (0)ساله درقلبت🌹😜♥", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "😐" and msg.get("author_object_guid") :
												bot.sendMessage(target, "چیه پوکرمیدی🤨", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "😐💔" and msg.get("author_object_guid") :
												bot.sendMessage(target, "💔😐", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "💔" and msg.get("author_object_guid") :
												bot.sendMessage(target, "😶", message_id=msg.get("message_id"))
												
					elif msg.get("text").startswith("😂") or msg.get("text").startswith("🤣"):
							try:
								bot.sendMessage(target, "جــون تـو فــقط بخـند😍", message_id=msg.get("message_id"))
							except:
								print("err luagh")
												
					elif msg.get("text") == "زئوس" and msg.get("author_object_guid") :
												bot.sendMessage(target, "جانا🙃", message_id=msg.get("message_id"))
												
					elif msg.get("text").startswith("چه خبر") or msg.get("text").startswith("چخبر"):
							try:
								bot.sendMessage(target, "ســلامـتیت😍♥", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")
												
					elif msg.get("text") == "فدات" and msg.get("author_object_guid") :
												bot.sendMessage(target, "نشی🤗", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "قربونت" and msg.get("author_object_guid") :
												bot.sendMessage(target, "♥🌹", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "بای":
						bot.sendMessage(target, "بای بای🖖🖖", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "خداحافظ":
						bot.sendMessage(target, "خداحافظ گل🌹🥺", message_id=msg.get("message_id"))	
						
					elif msg.get("text") == "س":
						bot.sendMessage(target, "س🗿", message_id=msg.get("message_id"))											
																			
												
																			
												
																							
												
				 
												
																																					
					elif msg.get("text") == "ربات" and msg.get("author_object_guid") :
												bot.sendMessage(target, "جانم😜", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "بات" and msg.get("author_object_guid") :
												bot.sendMessage(target, "نمی تونی درست صدام کنی😐", message_id=msg.get("message_id"))
												
												
																									



					elif msg.get("text").startswith("جوک"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text") == "تایم":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "تاریخ":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "حذف" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام پاک شد ✅", message_id=msg.get("message_id"))

					
					elif msg.get("text") == "گپ بسته" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "گپ بسته شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "گپ باز" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "گپ باز شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("ریم") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f"✅ کاربر حذف شد", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f"❎ کاربر حذف نشد", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f"کاربر حذف نشد ❌", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f"کاربر حذف شد ✅", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "روشن" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "ربات فعال شد ✅", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"اگه قوانین رو رعایت میکردی حذف نمیشدی !", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام کاربر {user}  به گروه {name} خوش اومدید 😃\nلطفا قوانین رو رعایت کن ✅                                               برای اطلاعات بیشتر از کلمه(قوانین)استفاده کنید😊‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌برای اطلاعات بیشتر دستورات ربات ازکلمه ایه /help", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"خدانگهدار {user} 🗑️", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام کاربر {user}  به گروه {name} خوش اومدید 😃\nلطفا قوانین رو رعایت کن ✅                                               برای اطلاعات بیشتر از کلمه(قوانین)استفاده کنید😊‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌برای اطلاعات بیشتر دستورات ربات ازکلمه ایه /help", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
