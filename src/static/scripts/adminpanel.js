

const header_elements = [
    {id:"header_1", name:"Dashboard"},
    {id:"header_1", name:"Settings"},
];


function ProfileCard(){
    return (
        <div className="CardCont">
            <h2>Public profile</h2>
            <form>
                <label>Name</label>
                <input type="text" id="new_nickname" name="nickname"></input>
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


function Header(){
    const elements = header_elements.map((element) =>
        <div onClick={() => location.replace("/admin/"+element.name)} key={element.id} className={(element.name == page) ? 'header_element header_element_choosed' : 'header_element'}>
            <h1>{element.name}</h1>
        </div>
    );
    return <>{elements}</>
}


function ShowPage(){
    switch (page) {
        case "Dashboard":
            return (
                <div className="page">
                    <h1>Dashboard</h1>
                </div>
            );
        case "Settings":
            return (
                <div className="page">
                    <ProfileCard />
                    <AccountCard />
                </div>
            );
        
    }
}

function App() {
    return (
    <div>
        <div className="header">
            <Header />
        </div>
        <ShowPage />
    </div>
    )
}



const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App />);