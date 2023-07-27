import streamlit as st

class Motherboard:
    def __init__(self, power, connection,ram):
        self.power = power
        self.connection = connection
        self.ram = ram

class CPU:
    def __init__(self, power, connection , cooling):
        self.power = power
        self.connection = connection
        self.cooling = cooling

class Fan:
    def __init__(self, cooling ):
        self.cooling = cooling

class Ram:
    def __init__(self,ram):
        self.ram =  ram

# Creating three objects per class
motherboards = [
    Motherboard(power=500, connection='Socket A',ram = 'DDR4'),
    Motherboard(power=750, connection='Socket B',ram = 'DDR4'),
    Motherboard(power=1000, connection='Socket C',ram = 'DDR4')
]

cpus = [
    CPU(power=500, connection='Socket A',cooling = 'big'),
    CPU(power=1000, connection='Socket B',cooling = 'little'),
    CPU(power=750, connection='Socket C',cooling = 'little')
]

fans = [
    Fan(cooling = 'big')
]

rams = [
    Ram(ram = 'DDR4')
]



#state conditions
if 'Motherboard' not in st.session_state:
    st.session_state['Motherboard'] = 0
if 'Cpu' not in st.session_state:
    st.session_state['Cpu'] = 0
if 'Ram' not in st.session_state:
    st.session_state['Ram'] = 0
if 'Fan' not in st.session_state:
    st.session_state['Fan'] = 0


#state output
if 'problempower' not in st.session_state:
    st.session_state['problempower'] = ''
if 'connection' not in st.session_state:
    st.session_state['connection'] = ''
if 'cooling' not in st.session_state:
    st.session_state['cooling'] = ''
if 'ramproblem' not in st.session_state:
    st.session_state['ramproblem'] = ''
#----------------------------------------------------------------

st.title("PC Builder")


# Displaying buttons for motherboards
st.subheader("Motherboards")
for i, motherboard in enumerate(motherboards):

    if st.button(f"Motherboard {i+1}"):

        st.session_state['Motherboard'] = i

        # Checking if power values are the same
        if motherboard.power == cpus[st.session_state['Cpu']].power:
            st.subheader("power Result: OK")
        else:
            st.subheader("power Result: no")


#show problems       
st.title(st.session_state['problempower']) 

motherboardNumber = st.session_state['Motherboard']


# Displaying buttons for CPUs
st.subheader("CPUs")
for i, cpu in enumerate(cpus):

    if st.button(f"CPU {i+1}"):

        st.session_state['Cpu'] = i

        # Checking if power values are the same
        if cpu.power == motherboards[motherboardNumber].power:
            st.subheader("power Result: OK")
        else:
            st.subheader("power Result: Not OK")

        if cpu.connection == motherboards[motherboardNumber].connection:
            st.subheader("connection Result: OK")
        else:
            st.subheader("connection Result: Not OK")


st.subheader("Rams")
for i, enurams in enumerate(rams):

    if st.button(f"Ram {i+1}"):

        st.session_state['Ram'] = i

        # Checking if power values are the same
        if enurams.ram == motherboards[motherboardNumber].ram:
            st.subheader('Good Ram')
        else:
            st.subheader('bad Ram')


st.subheader("Fans")
for i, enufans in enumerate(fans):

    if st.button(f"Fan {i+1}"):

        st.session_state['Fan'] = i

        # Checking if power values are the same
        if enufans.cooling == cpus[st.session_state['Cpu']].cooling:
            st.subheader('Good cooling')
        else:
            st.subheader('bad cooling')




# st.subheader(f"CPU problems found:{st.session_state['problempower']}")
# st.subheader(f"CPU problems found:{st.session_state['connection']}")

st.write(st.session_state['Motherboard'])