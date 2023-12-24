

const header_elements = [
    {id:1, name:"Dashboard"},
    {id:2, name:"Settings"}
]

function Header(){
    const elements = header_elements.map((element) =>
        <div onClick={() => location.replace("/admin/"+element.name)} key={element.id} className={(element.name == page) ? 'header_element header_element_choosed' : 'header_element'}>
            <h1>{element.name}</h1>
        </div>
    );
    return <>{elements}</>
}

function App() {
    return (
    <div>
        <div className="header">
            <Header />
        </div>
    </div>
    )
}



const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App />);