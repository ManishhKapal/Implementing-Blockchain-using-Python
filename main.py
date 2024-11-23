import streamlit as st
from blockchain import Blockchain

def main():
    st.title('Simple Blockchain Visualization')

    # Initialize the blockchain in the session state if it doesn't exist.
    if 'chain' not in st.session_state:
        st.session_state.chain = Blockchain()

    # Number input for the number of blocks to be created.
    n = st.number_input('Enter the number of blocks to be created:', min_value=1, step=1, format='%d')

    # Ensure block_data list is in the session state and has the correct length.
    if 'block_data' not in st.session_state or len(st.session_state.block_data) != n:
        st.session_state.block_data = [''] * n

    # Input data for each block.
    for x in range(n):
        st.session_state.block_data[x] = st.text_input(f'Enter data for block {x + 1}:', key=f'data_{x}')

    # Create Blockchain button.
    if st.button('Create Blockchain'):
        chain = st.session_state.chain
        # Add blocks with the provided data.
        for data in st.session_state.block_data:
            if data:
                chain.add_block(data)

        st.success('Blockchain created successfully!')

    # Display the blockchain.
    st.subheader('Blockchain Data')
    display_blockchain(st.session_state.chain)

def display_blockchain(chain):
    # Iterate through the blocks in the blockchain and display their details.
    for block in chain.chain:
        st.write(f"**Block {block.index}**")
        st.write(f"Timestamp: {block.real_time()}")
        st.write(f"Data: {block.data}")
        st.write(f"Hash: {block.hash}")
        st.write(f"Previous Hash: {block.previous_hash}")
        st.markdown("---")

if __name__ == '__main__':
    main()
