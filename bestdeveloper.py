import pyrebase
firebaseConfig = {
    'apiKey': "AIzaSyCbf9cl8V8gwA_ibxv6xvm55alsOUO2M6o",
    'authDomain': "nagapillaiyar.firebaseapp.com",
    'databaseURL': "https://nagapillaiyar-default-rtdb.firebaseio.com",
    'projectId': "nagapillaiyar",
    'storageBucket': "nagapillaiyar.appspot.com",
    'messagingSenderId': "131007437411",
    'appId': "1:131007437411:web:b5b4171435214efdc6f656",
    'measurementId': "G-CWG2MSW8YZ"
  }
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
auth = firebase.auth()
def createUser(email,password):
    user = auth.create_user_with_email_and_password(email, password)
    auth.send_email_verification(user['idToken'])
    return user
def signInUser(email,password):
    user = auth.sign_in_with_email_and_password(email, password)
def resetPassword(email):
    user = auth.send_password_reset_email("email")
def getUserInfo(idToken):
    return auth.get_account_info(idToken)
def addImageToBestStorage(cloudImage,localImage):
    storage.child(cloudImage).put(localImage)
