import numpy as np
import pickle
import streamlit as st
import warnings
import base64  # Import the base64 module to handle the image encoding

warnings.filterwarnings('ignore')

# Load the model
loaded_model = pickle.load(open("milk_model.sav", 'rb'))

# Function to add background from a local file
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image}");
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Use your local image file path
add_bg_from_local("Bc.jpg")

# Prediction function
def milkquality_prediction(input_data):
    try:
        input_data_np = np.asarray(input_data, dtype=np.float32).reshape(1, -1)
        prediction = loaded_model.predict(input_data_np)

        if prediction[0] == 1:
            return "𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐎𝐅 𝐓𝐇𝐄 𝐌𝐈𝐋𝐊 𝐈𝐒 𝐒𝐔𝐁𝐎𝐏𝐓𝐈𝐌𝐀𝐋. 𝐅𝐀𝐓 𝐂𝐎𝐍𝐓𝐄𝐍𝐓 𝐈𝐒 𝐋𝐎𝐖, 𝐀𝐍𝐃 𝐓𝐇𝐄 𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐆𝐎𝐎𝐃."
        elif prediction[0] == 2:
            return "𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐎𝐅 𝐓𝐇𝐄 𝐌𝐈𝐋𝐊 𝐈𝐒 𝐌𝐎𝐃𝐄𝐑𝐀𝐓𝐄. 𝐅𝐀𝐓 𝐂𝐎𝐍𝐓𝐄𝐍𝐓 𝐈𝐒 𝐀𝐕𝐄𝐑𝐀𝐆𝐄, 𝐀𝐍𝐃 𝐓𝐇𝐄 𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐈𝐒 𝐒𝐀𝐓𝐈𝐒𝐅𝐀𝐂𝐓𝐎𝐑𝐘."
        else:
            return "𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐎𝐅 𝐓𝐇𝐄 𝐌𝐈𝐋𝐊 𝐈𝐒 𝐄𝐗𝐂𝐄𝐋𝐋𝐄𝐍𝐓. 𝐅𝐀𝐓 𝐂𝐎𝐍𝐓𝐄𝐍𝐓 𝐈𝐒 𝐎𝐏𝐓𝐈𝐌𝐀𝐋, 𝐀𝐍𝐃 𝐓𝐇𝐄 𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐈𝐒 𝐒𝐔𝐏𝐄𝐑𝐈𝐎𝐑"
    except Exception as e:
        return f"Error in prediction: {e}"

def main():
    st.title('𝐌𝐢𝐥𝐤 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐏𝐫𝐞𝐝𝐢𝐜𝐭𝐢𝐨𝐧')
    
    # Input fields
    pH = st.text_input('𝐏𝐇 𝐋𝐄𝐕𝐄𝐋')
    Temperature = st.text_input('𝐓𝐄𝐌𝐏𝐄𝐑𝐀𝐓𝐔𝐑𝐄')
    Taste = st.text_input('𝐓𝐀𝐒𝐓𝐄 𝐋𝐄𝐕𝐄𝐋')
    Odor = st.text_input('𝐎𝐃𝐎𝐔𝐑 𝐋𝐄𝐕𝐄𝐋')
    Fat = st.text_input('𝐅𝐀𝐓 𝐋𝐄𝐕𝐄𝐋')
    Turbidity = st.text_input('𝐓𝐔𝐑𝐁𝐈𝐃𝐈𝐓𝐘')
    Colour = st.text_input('𝐂𝐎𝐋𝐎𝐑 𝐋𝐄𝐕𝐄𝐋 𝐎𝐅 𝐌𝐈𝐋𝐊')
    
    # Validate inputs and convert them to floats
    try:
        input_data = [
            float(pH),
            float(Temperature),
            float(Taste),
            float(Odor),
            float(Fat),
            float(Turbidity),
            float(Colour)
        ]
        input_valid = True
    except ValueError:
        st.error("Please enter valid numeric values for all input fields.")
        input_valid = False
    
    # Prediction code
    prediction_result = ''
    
    if input_valid and st.button('𝐏𝐑𝐄𝐃𝐈𝐂𝐓'):
        prediction_result = milkquality_prediction(input_data)
        
    st.success(prediction_result)

if __name__ == '__main__':
    main()