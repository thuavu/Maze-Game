const box = document.querySelector("#box");

let i = 0;
while(i < 10)
{
  console.log(i);
  i++;
}


let shiftLeft = 100;
let shiftTop = 100;

document.addEventListener("keydown", (event) => {
  if(event.key === "ArrowDown")
  {
    shiftTop = shiftTop + 2;
  }
  else if (event.key === "ArrowLeft")
  {
    shiftLeft = shiftLeft - 2;
  }
  else if (event.key === "ArrowUp")
  {
    shiftTop = shiftTop - 2;
  }
  else if (event.key === "ArrowRight")
  {
    shiftLeft = shiftLeft + 2;
  }
  box.style.left = shiftLeft + "px";
  box.style.top = shiftTop + "px";

});
