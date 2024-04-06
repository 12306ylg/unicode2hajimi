import streamlit as st
def decimal_to_base3(decimal_number:int):
    if decimal_number == 0:
        return "0"
    
    base3_number = ""
    
    while decimal_number > 0:
        remainder = decimal_number % 3
        base3_number = str(remainder) + base3_number
        decimal_number = decimal_number // 3
    
    return base3_number
def encrypt_char(char):
    """加密一个字符"""
    trinary = decimal_to_base3(ord(char))
    return ''.join(['哈' if digit == '0' else '基' if digit == '1' else '米' for digit in trinary])

def decrypt_char(encrypted):
    """解密一个字符"""
    trinary = ''.join(['0' if char == '哈' else '1' if char == '基' else '2' for char in encrypted])
    return chr(int(trinary, 3))


# Streamlit 应用代码
st.title('Unicode 加密和解密')

input_text_en = st.text_input('输入文本进行加密:')
input_text_de = st.text_input('输入文本进行解密:')
if input_text_en:
    encrypted_text = ' '.join(encrypt_char(c) for c in input_text_en)
    st.write('加密后的文本: ')
    st.write(encrypted_text)
if input_text_de:
    try:
        decrypted_text = ''.join(decrypt_char(c) for c in input_text_de.split())
        st.write('解密后的文本: ')
        st.write(decrypted_text)
    except OverflowError:
    except OverflowError:st.error('非法字符')