var header = [{"id":"header_1", "name":"Home"}, {"id":"header_2", "name":"Dashboard"}, {"id":"header_3", "name":"Settings"}, {"id":"header_4", "name":"AdminSettings"},]

function ShowPage(){
    console.log(page);
    switch (page) {
        
        case "Home":
            return (
                <div className="page">
                    <h1>Home</h1>
                </div>
            );
        case "Dashboard":
            return (
                <div className="page">
                    <h1>Dashboard</h1>
                    <SimpleCard />
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
                    <AddNewAdmin />
                </div>
            );
        
    }
}


// Admin Functions

function AddNewAdmin(){
    return(
        <div className="CardCont">
            <h2>Add new Admin</h2>
            <form>
                <label>Email of new admin</label>
                <input type="email" id="new_nickname" name="admin_email"></input>
                <button type="submit" value="Submit">Submit</button>
            </form>
        </div>
    );
}