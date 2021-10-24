import React from 'react';
import { useState, useEffect } from 'react';

export default function Sidebar({nearby, setNearby}) {
    const [libraries, setLibraries] = useState([])

    // useEffect(() => {
    //     fetch()
    //         .then(response => response.json()) 
    //         .then(data => {
    //             setLibraries(data);
    //         })
    //     }
    // , []);
    return (
        <div id="sidebar">
            <div id="sidebar-header">Available Libraries</div>
            {/* {libraries.map()} */}
        </div>
    )
}
