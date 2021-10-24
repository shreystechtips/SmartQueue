import React from 'react';
import { useState, useEffect } from 'react';

import Library from './Library';

const libraries = [
    {
      "id": "ChIJQ5poxV59hYARuD-jFIiXHP8",
      "Name": "Kresge Engineering Library",
      "popular_times": [{"name": "Monday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"name": "Tuesday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 20, 35, 49, 61, 71, 80, 81, 73, 53, 31, 14, 4, 0, 0]}, {"name": "Wednesday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 45, 64, 79, 83, 77, 66, 60, 61, 61, 51, 32, 15, 0, 0]}, {"name": "Thursday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 18, 35, 56, 73, 86, 94, 100, 98, 85, 62, 39, 20, 0, 0]}, {"name": "Friday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 30, 39, 38, 31, 28, 34, 47, 56, 50, 35, 18, 6, 0, 0]}, {"name": "Saturday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 15, 20, 19, 24, 35, 38, 25, 0, 0, 0, 0, 0, 0, 0]}, {"name": "Sunday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 47, 50, 44, 44, 37, 24, 10, 2, 0, 0]}],
    "coords":{"lat":0,"lng":0},
    "url": "https://www.google.com/maps/place/?q=place_id:ChIJQ5poxV59hYARuD-jFIiXHP8",
    "current_popularity": 55,
    "distance": 0
    },
    {
        "id": "ChIJQ5poxV59hYARuD-jFIiXHP8",
        "Name": "Kresge Engineering Library",
        "popular_times": [{"name": "Monday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"name": "Tuesday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 20, 35, 49, 61, 71, 80, 81, 73, 53, 31, 14, 4, 0, 0]}, {"name": "Wednesday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 45, 64, 79, 83, 77, 66, 60, 61, 61, 51, 32, 15, 0, 0]}, {"name": "Thursday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 18, 35, 56, 73, 86, 94, 100, 98, 85, 62, 39, 20, 0, 0]}, {"name": "Friday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 30, 39, 38, 31, 28, 34, 47, 56, 50, 35, 18, 6, 0, 0]}, {"name": "Saturday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 15, 20, 19, 24, 35, 38, 25, 0, 0, 0, 0, 0, 0, 0]}, {"name": "Sunday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 47, 50, 44, 44, 37, 24, 10, 2, 0, 0]}],
      "coords":{"lat":0,"lng":0},
      "url": "https://www.google.com/maps/place/?q=place_id:ChIJQ5poxV59hYARuD-jFIiXHP8",
      "current_popularity": 55,
      "distance": 0
      },
      {
        "id": "ChIJQ5poxV59hYARuD-jFIiXHP8",
        "Name": "Kresge Engineering Library",
        "popular_times": [{"name": "Monday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"name": "Tuesday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 20, 35, 49, 61, 71, 80, 81, 73, 53, 31, 14, 4, 0, 0]}, {"name": "Wednesday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 45, 64, 79, 83, 77, 66, 60, 61, 61, 51, 32, 15, 0, 0]}, {"name": "Thursday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 18, 35, 56, 73, 86, 94, 100, 98, 85, 62, 39, 20, 0, 0]}, {"name": "Friday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 30, 39, 38, 31, 28, 34, 47, 56, 50, 35, 18, 6, 0, 0]}, {"name": "Saturday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 15, 20, 19, 24, 35, 38, 25, 0, 0, 0, 0, 0, 0, 0]}, {"name": "Sunday", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 47, 50, 44, 44, 37, 24, 10, 2, 0, 0]}],
      "coords":{"lat":0,"lng":0},
      "url": "https://www.google.com/maps/place/?q=place_id:ChIJQ5poxV59hYARuD-jFIiXHP8",
      "current_popularity": 55,
      "distance": 0
      },
]

export default function Sidebar({nearby, setNearby}) {
    // const [libraries, setLibraries] = useState([])

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
            <div id="sidebar-libraries">
                {libraries.map(info => <Library key={info.id} info={info} />)}
            </div>
        </div>
    )
}
