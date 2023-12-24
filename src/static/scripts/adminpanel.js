

const header_elements = [
    {id:1, name:"Dashboard"},
    {id:2, name:"Settings"},
    {id:3, name:"Profile"},
    
]

function Header(){
    const elements = header_elements.map((element) =>
        <div onClick={() => location.replace("/admin/"+element.name)} key={element.id} className={(element.name == page) ? 'header_element header_element_choosed' : 'header_element'}>
            <h1>{element.name}</h1>
        </div>
    );
    return <>{elements}</>
}


function ShowPage(){
    if (page == "Settings"){
        return (
        <div className="Settings_page">
            <h1>Settings</h1>
        </div>
        );
    }
    if (page == "Dashboard"){
        return (
        <div className="Settings_page">
            <h1>Dashboard</h1>
        </div>
        );
    }
    if (page == "Profile"){
        return (
        <div className="Settings_page">
            <h1>Profile</h1>
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