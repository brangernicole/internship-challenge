import React from 'react'
import { useTheme } from './context/ThemeContext'
import LCMForm from './components/LCMForm'
import { Button } from './components/ui/button'
import { Card } from './components/ui/card'
import { Moon, Sun } from 'lucide-react'

export default function App() {
  const { theme, toggleTheme } = useTheme()

  return (
    <div className="min-h-screen bg-background text-foreground">
      <div className="absolute top-4 right-4">
        <Button
          variant="outline"
          size="icon"
          onClick={toggleTheme}
          aria-label="Toggle theme"
        >
          {theme === 'light' ? (
            <Moon className="h-4 w-4" />
          ) : (
            <Sun className="h-4 w-4" />
          )}
        </Button>
      </div>

      <div className="flex items-center justify-center min-h-screen p-6">
        <div className="w-full max-w-lg">
          <Card className="p-8">
            <div className="text-center mb-8">
              <h1 className="text-4xl font-bold mb-2">🔢 Calculadora MMC</h1>
              <p className="text-muted-foreground">Encontre o Mínimo Múltiplo Comum</p>
            </div>
            <LCMForm />
          </Card>
        </div>
      </div>
    </div>
  )
}
