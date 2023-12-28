
function ProfileCard(){
    return (
        <div className="CardCont">
            <h2>Public profile</h2>
            <form action="/setfullname" method="post">
                <label>Full Name</label>
                <input type="text" id="new_fullname" name="new_fullname" defaultValue={fullname} onChange={(e) => setFullname(e.target.value)}></input>
                <label className="description_label">Your name may appear around GitHub where you contribute or are mentioned. You can remove it at any time. </label>
                <button type="submit" value="Submit">Update Profile</button>
            </form>
        </div>
    );
}

function AccountCard(){
    return (
        <div className="CardCont">
            <h2>Change password</h2>
            <form action="/setnewpass" method="post">
                <label>New password</label>
                <input type="text" id="username_in_change_pass" name="username" value={username}></input>
                <input type="password" id="password" name="password"></input>
                <label>Retype new password</label>
                <input type="password" id="retyped-password" name="retyped-password"></input>
                <label className="description_label">Your name may appear around GitHub where you contribute or are mentioned. You can remove it at any time. </label>
                <button type="submit" value="Submit">Change password</button>
            </form>
        </div>
    );
}

// TODO: maybe i do it in future, now it not needed
function SimpleCard(){
    return(
        <div className="CardCont">
            <h2>Simple Card Example</h2>
            <form>
                <label className="description_label">the card just write number to DB here you can test SQL injection</label>
                <input type="text" id="new_nickname" name="nickname" value="1"></input>
                <div>
                    <button type="submit" value="Submit">+</button>
                    <button type="submit" value="Submit">-</button>
                </div>
            </form>
        </div>
    );
}

function Logout(){
    return(
        <h2 key="logout_button" onClick={() => location.replace("/logout")} >logout</h2>
    )
}


function TrigerMenu() {
    if (document.getElementById("small_header").style.display == "flex"){
        document.getElementById("small_header").style.display = "none";
        
    }
    else{
        document.getElementById("small_header").style.display = "flex";
    }
}

function MenuButton(){
    return(
    <div className="menu-button" id="menu-button" onClick={TrigerMenu}>
        <i class="fa-solid fa-bars"></i>
    </div>
    )
}
function Header(){
    console.log(pages_to_show);
    
    const elements = header.map((element) =>
        <div onClick={() => location.replace("/"+element.name)} key={element.id} className={(element.name == page) ? 'header_element header_element_choosed' : 'header_element'}>
            <h1 key={element.id+"_TEXT"}>{element.name}</h1>
        </div>
    );
    return (<div className="header" key="header">
        <MenuButton />
        <div className="header_pages" key="header_pages">
            {elements} 
        </div>
        <Logout />
    </div>);
}

function HeaderForSmallDevices(){
    const elements = header.map((element) =>
        <div onClick={() => location.replace("/"+element.name)} key={element.id} className={(element.name == page) ? 'small_header_element small_header_element_choosed' : 'small_header_element'}>
            <h1 key={element.id+"_TEXT"}>{element.name}</h1>
        </div>
    );
    return (<div className="small_header" key="small_header" id="small_header">{elements}</div>);
}

function App() {
    return(
        <>
            <Header/>
            <HeaderForSmallDevices />
            {error && (
                        <div className="error_div error_margin" >
                        <h3>{error}</h3>
                        <h4>{error_desc}</h4>
                        </div>
                    )}
            {info && (
                        <div className="info_div info_margin" >
                        <h3>{info}</h3>
                        <h4>{info_desc}</h4>
                        </div>
                    )}
            <ShowPage />
        </>
    );
}
const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App />);