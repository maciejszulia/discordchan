import random

# p_msg = private_message
def get_response(msg: str) -> str:
    p_msg = msg.lower()
    if p_msg == 'ksalol':
        return 'leczy banie'
    
    if msg == 'ksalol':
        return 'nie leczy bani'
    
    if p_msg == '!help' or p_msg == '!h':
        return 'sraka'
    
    return 'None'