import {React, useState} from 'react'

const descriptions = [
    "The library is ✨open✨",
    "So you don't have to sit on the library floor",
    "Convenient libraries, for your convenience"
]

export default function Title() {
    const [descIndex, setDescIndex] = useState(Math.floor(Math.random() * descriptions.length))
    const toggleDescIndex = () => setDescIndex((descIndex + 1) % 3)
    return (
        <div id="title" onClick={toggleDescIndex}>
            <div id="title-header">
                Cal Study Spaces
            </div>

            <div id="title-description">
                {/* The library is ✨open✨ */}
                {descriptions[descIndex]}
            </div>
        </div>

    
    )
}
