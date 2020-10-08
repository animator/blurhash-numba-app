import streamlit as st
st.set_option('deprecation.showfileUploaderEncoding', False)

import numpy as np
from PIL import Image
import blurhash_numba as bnb


st.title('blurhash-numba')
st.subheader('The fastest BlurHash Python implementation')

option = st.sidebar.selectbox(
    'Select Demo:',
     ("Encoding", "Decoding"))

if option == "Encoding":
    """

    ### Encoding Demo

    """

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        image_array = np.array(image.convert("RGB"), dtype=np.float)
        xc = st.slider("Choose X-components: ", min_value=1,   
                       max_value=9, value=4, step=1)
        yc = st.slider("Choose Y-components: ", min_value=1,   
                       max_value=9, value=3, step=1)
        blurhash_code = bnb.encode(image_array, x_components = xc, y_components = yc)
        """

        ### Generated BlurHash

        """
        st.code(blurhash_code, language="json")

if option == "Decoding":
    """

    ### Decoding Demo

    """

    blurhash_code = st.text_input("Enter BlurHash String...")

    if len(blurhash_code) >= 6:
        """

        ### Generated Image

        """
        blur_img = Image.fromarray(np.array(bnb.decode(blurhash_code, 256, 256)).astype('uint8'))
        st.image(blur_img, caption='Generated Image.', use_column_width=True)