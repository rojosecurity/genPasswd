export function clipboard(){
    var clip = document.getElementById("clipboard")
    var btncopiar = document.getElementById("btnCopiar")

    btncopiar.addEventListener('click',async function(){
        
        try{
            await navigator.clipboard.writeText(clip.textContent)
            
            alert("Contraseña Copiada")

        }catch(e){
            console.error("error al copiar",e)
        }
        
    }) 
}

clipboard() 

