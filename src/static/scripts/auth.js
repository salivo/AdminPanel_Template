function App() {
    if (register == "true"){
        return(
            <div className="AuthCard">
                
                <form method="post" className="AuthinCard">
                    <h2>Register</h2>
                    <label>Fullname</label>
                    <input required type="text" name="fullname"></input>
                    <label>Username</label>
                    <input required type="text" name="username"></input>
                    <label>Email</label>
                    <input required type="email" name="email"></input>
                    <label>Password</label>
                    <input required type="password" name="password"></input>
                    <div>
                        <label className="description_label">Or you can login <a href="/login">here</a></label>
                        <button>Create Acount</button>
                    </div>
                </form>
            </div>
            );
    }
    else{
        return(
            <div className="AuthCard">

                <form method="post" className="AuthinCard">
                    <h2>Login</h2>
                    <label>Username or Email</label>
                    <input type="email" required name="username"></input>
                    <label>Password</label>
                    <input type="password" required name="password"></input>
                    <div>
                        <label className="description_label">Or you can register <a href="/register">here</a></label>
                        <button>Login</button>
                    </div>
                </form>
            </div>
            );
    }
}

const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App />);