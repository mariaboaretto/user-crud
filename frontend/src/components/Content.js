import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import TopSection from './TopSection';
import UserList from './UserList';

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