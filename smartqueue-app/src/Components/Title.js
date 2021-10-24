import {React, useState} from 'react'

const descriptions = [
    "The library is ✨open✨",
    "So you don't have to sit on the library floor",
    "Convenient libraries, for your convenience"
]

export default function Title({ setPage, setLat, setLng }) {
    const [descIndex, setDescIndex] = useState(Math.floor(Math.random() * descriptions.length))

    const toggleDescIndex = () => setDescIndex((descIndex + 1) % 3)
    function handleClick() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(getData);
            
        } else {
           return false;
        }
    }

    function getData(position) {
        setLat(position.coords.latitude);
        setLng(position.coords.longitude);
        setPage('nearby')
    };
    return (
        <div id="title">
            <div id="title-header">
            Libearium  
            </div>

            <div id="title-description" onClick={toggleDescIndex}>
                {descriptions[descIndex]}
            </div>
            <button id="title-button" onClick={handleClick}>
                Nearby Locations
            </button>
        </div>

    
    )
}
