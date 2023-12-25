var header = [{"id":"header_1", "name":"Home"},{"id":"header_2", "name":"Settings"}]

function ShowPage(){
    console.log(page);
    switch (page) {
        
        case "Home":
            return (
                <div className="page">
                    <h1>Home</h1>
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