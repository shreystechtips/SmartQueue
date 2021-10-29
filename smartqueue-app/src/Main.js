import {React, useState} from 'react'
import Sidebar from './Components/Sidebar'
import Home from './Components/Home'

export default function Main() {
    const [page, setPage] = useState('home');
    const [lat,setLat] = useState(null);
    const [lng,setLng] = useState(null);

    return (
        <div id="main">
            <Home setPage={setPage} setLat={setLat} setLng={setLng} />
            <Sidebar page={page} lat={lat} lng={lng} setPage={setPage} />
        </div>
    )
}
