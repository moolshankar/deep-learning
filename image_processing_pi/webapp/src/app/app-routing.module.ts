import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DisplayInfoComponent } from './display-info/display-info.component';
import { RegisterVisitorComponent } from './register-visitor/register-visitor.component';
import { ScanComponent } from './scan/scan.component';

const routes: Routes = [
  { path: '', component: ScanComponent },
  { path: 'display', component: DisplayInfoComponent },
  { path: 'register', component: RegisterVisitorComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
