import {React, useState} from 'react'
import Sidebar from './Components/Sidebar'
import Title from './Components/Title'

const pages = ['home', 'nearby']

export default function Home() {
    const [page, setPage] = useState('home');
    const [lat,setLat] = useState(null);
    const [lng,setLng] = useState(null);

    return (
        <div id="home">
            <div className="circle" id="circle-1">
                <Title setPage={setPage} setLat={setLat} setLng={setLng} />
            </div>
            <div className="circle" id="circle-2" />
            <div className="circle" id="circle-3" />
        
            <Sidebar page={page} lat={lat} lng={lng} setPage={setPage} />
        </div>
    )
}
