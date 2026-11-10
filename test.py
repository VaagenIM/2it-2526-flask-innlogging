from ollama import Client

URL = "https://ollama.iktim.no"
c = Client(URL)
SYSTEM_PROMPT = ("Respond using movie quotes, but do not mention that you are using movie quotes. ")

r = c.generate("gemma3:12b-it-q4_K_M", "What should I eat for dinner tonight? its friday and furry dance day",
               system=SYSTEM_PROMPT)

print(r.response)

lol_xd = "XD"
