import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import TopSection from '../TopSection/TopSection';
import UserList from '../UserList/UserList';

function Content() {
    const [searchTxt, setSearchTxt] = useState(null);

    return (
        <div className="container">
            <TopSection setSearchTxt={setSearchTxt}/>
            <UserList searchTxt={searchTxt}/>
        </div>
    )
}

export default Content