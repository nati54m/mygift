import streamlit as st

# --- הגדרות ---
# 🔒 שנה את הסיסמה הסודית שלך כאן
SECRET_PASSWORD = "2012" 

# 🎁 שנה את המתנות שלך כאן
GIFT_1 = "יום ספא זוגי מפנק"
GIFT_2 = "סופשבוע בצימר בצפון"
GIFT_3 = "קורס בישול "
GIFT_4= 'חאתול'
GIFT_5= "סרט ויאיפי  "
GIFT_6= "ארוחה ביתית  "
GIFT_6= "בית מלון   "
# --- סוף הגדרות ---

# משתמש בזיכרון של הסשן כדי לדעת אם המשתמש מחובר
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- 1. דף הכניסה ---
if not st.session_state['logged_in']:
    st.title("מתנה סודית מחכה לך... 🎁")
    
    # שדה להזנת סיסמה
    user_password = st.text_input("הקלידי את הסיסמה הסודית:", type="password")
    
    # כפתור כניסה
    if st.button("כניסה"):
        if user_password == SECRET_PASSWORD:
            st.session_state['logged_in'] = True
            st.rerun() # מרענן את הדף כדי לעבור לשלב הבא
        else:
            st.error("סיסמה לא נכונה... נסי שוב!")

# --- 2. דף המתנות (אם מחוברים) ---
else:
    st.title("מזל טוב ליום ההולדת! ❤️")
    st.header("בבקשה בחרי את המתנה שלך:")
# כפתורים לבחירת מתנה
    if st.button(GIFT_1):
        st.session_state['gift_choice'] = GIFT_1

    if st.button(GIFT_2):
        st.session_state['gift_choice'] = GIFT_2

    if st.button(GIFT_3):
        st.session_state['gift_choice'] = GIFT_3
    
    # --- 3 הכפתורים החדשים ---
    if st.button(GIFT_4):
        st.session_state['gift_choice'] = GIFT_4

    if st.button(GIFT_5):
        st.session_state['gift_choice'] = GIFT_5

    if st.button(GIFT_6):
        st.session_state['gift_choice'] = GIFT_6
    # --- סוף הכפתורים החדשים ---
  
    # מציג את הבחירה שנבחרה
    if 'gift_choice' in st.session_state:
        st.balloons() # אפקט בלונים חמוד!
        st.success(f"בחירה מעולה! תתכונני ל: {st.session_state['gift_choice']}")
        st.write("\nאוהב המון, נתנאל")
