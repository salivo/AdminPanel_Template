var header = [{"id":"header_1", "name":"Home"}, {"id":"header_2", "name":"Dashboard"}, {"id":"header_3", "name":"Settings"}, {"id":"header_4", "name":"AdminSettings"},]

function ShowPage(){
    console.log(page);
    switch (page) {
        
        case "Home":
            return (
                <div className="page">
                    <h1>Hello {fullname}!</h1>
                </div>
            );
        case "Dashboard":
            return (
                <div className="page">
                    <h1>Here can be stats or another info for personal</h1>
                </div>
            );
        case "Settings":
            return (
                <div className="page">
                    <ProfileCard />
                    <AccountCard />
                </div>
            );
        case "AdminSettings":
            return (
                <div className="page">
                    <SetPermsLevel />
                </div>
            );
        
    }
}


// Admin Functions

function SetPermsLevel(){
    return(
        <div className="CardCont">
            <h2>Set Permision level for User</h2>
            <form action="/setpermslevel" method="post">
                <label>username</label>
                <input type="text" id="username" name="username"></input>
                <label>Permission level</label>
                <input type="number" id="level" name="level" 
                    min="0" max="1000"></input>
                <button type="submit" value="Submit">Submit</button>
            </form>
        </div>
    );
}