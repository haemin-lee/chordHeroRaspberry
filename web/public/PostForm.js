import React,{useState} from 'react';
import Axios from 'axios';


function PostForm(){
  const url ="" //needs to add url
  const[data,setData]=useState({
    song:""
  })

  function submit(e){
    e.preventDefault();
    Axios.post(url,{
      song: data.song
    })
      .then(res=>{
        console.log(res.data)
      })

  }
  function handle(e){
    const newdata={...data}
    newdata[e.target.song]=e.target.value
    setData(newdata)
    console.log(newdata)
  }
    return(
      <form action="" method="post">
        <input onChange={(e)=>handle(e)} type = "text" id="song request" name="song" value={data.song}><br>
        <inpit onChange={(e)=>handle(e)} type="submit" value="submit">
      </form>
    );


}



export default PostForm;
