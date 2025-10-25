import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { toast } from "sonner";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "./ui/form";
import { Input } from "./ui/input";
import { Button } from "./ui/button";

const lcmSchema = z.object({
  x: z
    .string()
    .min(1, "x é obrigatório")
    .regex(/^\d+$/, "x deve ser um número inteiro")
    .transform((val) => parseInt(val, 10))
    .pipe(z.number().int().positive("x deve ser maior que 0")),
  y: z
    .string()
    .min(1, "y é obrigatório")
    .regex(/^\d+$/, "y deve ser um número inteiro")
    .transform((val) => parseInt(val, 10))
    .pipe(z.number().int().positive("y deve ser maior que 0")),
});

export default function LCMForm() {
  const [result, setResult] = useState(null);

  const form = useForm({
    resolver: zodResolver(lcmSchema),
    defaultValues: { x: "1", y: "10" },
    mode: "onSubmit",
  });

  async function onSubmit(data) {
    setResult(null);

    // Validação adicional: x <= y
    if (data.x > data.y) {
      toast.warning("x deve ser menor ou igual a y");
      return;
    }

    try {
      const params = new URLSearchParams({ x: data.x, y: data.y });
      const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000";
      const res = await fetch(`${apiUrl}/api/lcm/?${params.toString()}`);
      if (!res.ok) throw new Error(`API retornou ${res.status}`);
      const json = await res.json();
      setResult(json.result);
      toast.success(`MMC calculado: ${json.result}`);
    } catch (e) {
      toast.error(`Erro ao calcular: ${e.message}`);
    }
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
        <div className="grid grid-cols-2 gap-4">
          <FormField
            control={form.control}
            name="x"
            render={({ field }) => (
              <FormItem>
                <FormLabel>x</FormLabel>
                <FormControl>
                  <Input placeholder="1" type="text" inputMode="numeric" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="y"
            render={({ field }) => (
              <FormItem>
                <FormLabel>y</FormLabel>
                <FormControl>
                  <Input placeholder="10" type="text" inputMode="numeric" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
        </div>

        <div className="flex gap-2">
          <Button type="submit" className="flex-1">
            {form.formState.isSubmitting ? "Calculando..." : "Calcular MMC"}
          </Button>
          <Button
            type="button"
            variant="outline"
            onClick={() => {
              form.reset();
              setResult(null);
            }}
          >
            Limpar
          </Button>
        </div>

        {result !== null && (
          <div className="p-6 bg-primary/10 border border-primary/20 rounded-lg">
            <p className="text-sm font-semibold text-primary mb-2">✓ Resultado</p>
            <p className="text-lg font-semibold text-foreground whitespace-pre-wrap break-words">
              {JSON.stringify(result, null, 2)}
            </p>
          </div>
        )}
      </form>
    </Form>
  );
}
