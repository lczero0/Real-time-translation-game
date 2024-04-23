# pip install baidu-aip
from aip import AipSpeech
import speech_recognition as sr

# 上一篇文章介绍的获取的Key值
APP_ID = '62558837'
API_KEY = 'Nh08DCySno8W4WCwyrRsgHA4'
SECRET_KEY = 'sGt6UFNyWUBZIpGqONMNY1mmqCsj60Uj'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_text(wav_bytes):
    result = client.asr(wav_bytes, 'wav', 16000, {'dev_pid': 1537, })
    try:
        text = result['result'][0]
    except Exception as e:
        print(e)
        text = ""
    return text


r = sr.Recognizer()
mic = sr.Microphone()
print("请说话...")

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout=10)
    print("录制中")

print("识别中...")
audio_data = audio.get_wav_data(convert_rate=16000)

print("\n正在分析...")

text = get_text(audio_data)
print(text)
