import { Router, Route, Switch } from "wouter";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { Toaster } from "@/components/ui/toaster";
import HomePage from "@/pages/HomePage";
import TemplatesPage from "@/pages/TemplatesPage";
import EditorPage from "@/pages/EditorPage";
import MyGraphicsPage from "@/pages/MyGraphicsPage";
import Navbar from "@/components/Navbar";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      queryFn: async ({ queryKey }) => {
        const response = await fetch(queryKey[0] as string);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      },
    },
  },
});

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <div className="min-h-screen bg-gray-50">
          <Navbar />
          <main className="container mx-auto px-4 py-8">
            <Switch>
              <Route path="/" component={HomePage} />
              <Route path="/templates" component={TemplatesPage} />
              <Route path="/editor/:templateId" component={EditorPage} />
              <Route path="/my-graphics" component={MyGraphicsPage} />
              <Route>
                <div className="text-center py-20">
                  <h1 className="text-2xl font-bold text-gray-800">Page not found</h1>
                  <p className="text-gray-600 mt-2">The page you're looking for doesn't exist.</p>
                </div>
              </Route>
            </Switch>
          </main>
        </div>
      </Router>
      <Toaster />
    </QueryClientProvider>
  );
}