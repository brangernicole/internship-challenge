import * as React from "react";
import { cn } from "../../lib/utils";

const Input = React.forwardRef(({ className, type = "text", inputMode, onInput, onChange, ...props }, ref) => {
  const handleInput = (e) => {
    // Se for numeric, bloqueia tudo que não for dígito
    if (inputMode === "numeric") {
      e.target.value = e.target.value.replace(/[^0-9]/g, "");
    }
    onInput?.(e);
  };

  const handleChange = (e) => {
    // Se for numeric, bloqueia tudo que não for dígito
    if (inputMode === "numeric") {
      e.target.value = e.target.value.replace(/[^0-9]/g, "");
    }
    onChange?.(e);
  };

  return (
    <input
      type={type}
      inputMode={inputMode}
      className={cn(
        "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      ref={ref}
      onInput={handleInput}
      onChange={handleChange}
      {...props}
    />
  );
});
Input.displayName = "Input";

export { Input };
