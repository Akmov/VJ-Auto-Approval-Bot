# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22440762"))
    API_HASH = getenv("API_HASH", "f18c585387a50ef82cf4eab05be6dd59")
    BOT_TOKEN = getenv("BOT_TOKEN", "6797040646:AAGOeZ8AFsdCda2U6qBy4mKm3GlXgD_NxTQ")
    FSUB = getenv("FSUB", "SM_Linkz")
    CHID = int(getenv("CHID", "-1001298919400"))
    SUDO = list(map(int, getenv("SUDO", "1361111830").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://autov4:autov4@cluster0.y95wsi4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
