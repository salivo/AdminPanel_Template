
function ProfileCard(){
    return (
        <div className="CardCont">
            <h2>Public profile</h2>
            <form>
                <label>Name</label>
                <input type="text" id="new_nickname" name="nickname" value={fullname}></input>
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
            <form>
                <label>New password</label>
                <input type="text" id="new_nickname" name="nickname"></input>

                <label>Confirm new password</label>
                <input type="text" id="new_nickname" name="nickname"></input>
                <label className="description_label">Your name may appear around GitHub where you contribute or are mentioned. You can remove it at any time. </label>
                <button type="submit" value="Submit">Change password</button>
            </form>
        </div>
    );
}

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

function Header(){
    console.log(pages_to_show);
    
    const elements = header.map((element) =>
        <div onClick={() => location.replace("/"+element.name)} key={element.id} className={(element.name == page) ? 'header_element header_element_choosed' : 'header_element'}>
            <h1 key={element.id+"_TEXT"}>{element.name}</h1>
        </div>
    );
    return (<div className="header" key="header">
        <div className="header_pages" key="header_pages">
            {elements} 
        </div>
        <Logout />
    </div>);
}




function App() {
    return(
        <>
            <Header/>
            <ShowPage />
        </>
    );
}
const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App />);