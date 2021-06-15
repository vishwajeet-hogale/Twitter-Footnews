

import React from 'react'

const Card = (text) => {
//  const [tweets, settweets] = useState([]);
  
  return ( 
    <div className="card">
      <h3>{text.text}</h3>
    </div>
  )
}

export default Card
