import { Link, useLocation } from "wouter";
import { Button } from "@/components/ui/button";
import { Palette, Home, Layout, Image } from "lucide-react";

export default function Navbar() {
  const [location] = useLocation();

  const navItems = [
    { href: "/", label: "Home", icon: Home },
    { href: "/templates", label: "Templates", icon: Layout },
    { href: "/my-graphics", label: "My Graphics", icon: Image },
  ];

  return (
    <nav className="bg-white shadow-sm border-b">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link href="/">
            <div className="flex items-center space-x-2">
              <Palette className="h-8 w-8 text-blue-600" />
              <span className="text-xl font-bold text-gray-900">GraphicsPro</span>
            </div>
          </Link>
          
          <div className="flex items-center space-x-4">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = location === item.href;
              
              return (
                <Link key={item.href} href={item.href}>
                  <Button
                    variant={isActive ? "default" : "ghost"}
                    className="flex items-center space-x-2"
                  >
                    <Icon className="h-4 w-4" />
                    <span>{item.label}</span>
                  </Button>
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </nav>
  );
}