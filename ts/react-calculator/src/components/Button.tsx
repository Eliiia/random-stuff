import { CSSProperties } from "react";

function NumberButton(props: {[k: string]: number}) {
    let n = props.number
    let styles: CSSProperties = {}
  
    if(n === 0) styles.gridColumn = 1
    if(n%3 === 0) styles.gridColumn = 3
    else styles.gridColumn = n%3

    return (
      <div className="button" style={styles}>
        <h1>{n}</h1>
      </div>
    );
  }
  
export { NumberButton };
  