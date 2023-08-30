css = '''
<style>
.chat-message {
    padding: 0.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.bot {
    background-color: #3f4570
}
.chat-message.user {
    background-color: #6e1929 
}
.chat-message .avatar {
  width: 10%;
}
.chat-message .avatar img {
  max-width: 50px;
  max-height: 50px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 85%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712104.png">
    </div>
    <div class="message">{{MSG}}</div>
</div> 
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn0.iconfinder.com/data/icons/users-android-l-lollipop-icon-pack/24/user-512.png">
    </div>
    <div class="message">{{MSG}}</div>
</div> 
'''
