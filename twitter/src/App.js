import Card from '../src/components/Card';
import React,{useState,useEffect} from 'react';

function App() {
  const [tweets, settweets] = useState([]);
  useEffect(()=>{
    const setID = setInterval(()=>{
      loadData();
    },1000);
    return () => clearInterval(setID);
  },[]);

  const loadData = async () =>{
    const response = await fetch("http://127.0.0.1:5000/fetch");
    const data = await response.json();
    console.log(data.data);
    let all = []
    data.data.forEach(item => {all.push(item["text"])});
    console.log(all.reverse());
    settweets(all);

  }
  return (
    <div className="booklist">
       {
        tweets.map((tweet) => {
          // const r = b.json();
          console.log(tweet);
          return <Card  text ={tweet} ></Card>
        })
      
      }
    </div>
     
    
  );
}

export default App;
