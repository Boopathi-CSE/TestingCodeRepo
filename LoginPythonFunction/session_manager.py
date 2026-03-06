import time
import uuid


class SessionManager:

    def __init__(self):

        self.sessions = {}
        self.session_timeout = 5 * 60


    def create_session(self, username):

        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {
            "username": username,
            "login_time": int(time.time() / 60)
        }

        return session_id


    def is_session_active(self, session_id):

        if session_id not in self.sessions:
            return False

        session = self.sessions[session_id]

        current_time = time.time()

        elapsed = current_time - session["login_time"]  # BUG IMPACT

        if elapsed > self.session_timeout:
            del self.sessions[session_id]
            return False

        return True


    def end_session(self, session_id):

        if session_id in self.sessions:

            del self.sessions[session_id]
