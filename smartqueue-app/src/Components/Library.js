import {useState} from 'react'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCaretDown, faCaretUp } from '@fortawesome/free-solid-svg-icons'

const busyThreshold = 20;

const getHourRange = hours => {
    let ranges = []
    let inRange = false
    let currentRange = []
    for (let i = 0; i < hours.length; i++) {
        if (hours[i] > busyThreshold && !inRange) {
            inRange = true;
            currentRange.push(i + 1)
        } else if (hours[i] < busyThreshold && inRange) {
            inRange = false;
            currentRange.push(i)
            ranges.push(currentRange)
            currentRange = []
        }
    }
    if (currentRange.length === 1) {
        currentRange.push(24);
        ranges.push(currentRange);
    }
    return ranges
}

const hourToString = hour => {
    if (hour <= 12) {
        return String(hour) + ":00 AM"
    } else {
        return String(hour - 12) + ":00 PM"
    }
}

const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
export default function Library({info}) {
    const [expanded, setExpanded] = useState(false);
    const toggleExpanded = () => setExpanded(!expanded);

    let day = new Date().getDay()
    let shifted = day === 0 ? 6 : day - 1
    var dayOfInterest = {};

    let hourRanges =  info.popular_times.length == 7 ? getHourRange(info.popular_times[shifted].data)  : []

    let expandInfo = (
        <div className="library-extra">
            <div className="library-times">
                <div className="library-times-title">Busy Times:</div>
            <div className="library-times-ranges">{hourRanges.map(range =>
            hourToString(range[0]) + " - " + hourToString(range[1]))}
            </div>
            </div>
            <a className="library-location" href={info.url} target="_blank" rel="noreferrer">
                Location
            </a>
        </div>
    )
    return (
        <div className="library" onClick={toggleExpanded}>
            <div className="library-left">
                <div className="library-name">{info.name}</div>
                <div className="library-popularity">Busyness Level: {info.popularity}%
                </div>
            
                {expanded ? expandInfo : <span />}
            </div>
            
            <FontAwesomeIcon icon={expanded ? faCaretUp : faCaretDown}className="library-drop" />
        </div>
    )
}
